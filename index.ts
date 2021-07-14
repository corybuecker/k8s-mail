import generate_x509 from './src/certificate'
import { chmod, writeFile, rm, readFile, readdir } from 'fs/promises'
import writePassword from './src/password_generator'

const yaml = require('js-yaml')
const readlineSync = require('readline-sync')

async function createVolumeFile(file: string, contents: string) {
  await rm(file, { force: true })
  await writeFile(file, contents, { flag: 'w+' })
  chmod(file, 0o444)
}

const secretTemplate = {
  apiVersion: 'v1',
  kind: 'Secret',
  metadata: {
    name: 'k8s-mail-secrets',
    namespace: 'k8s-mail',
  },
  data: {}
}

const program = async () => {
  console.info("starting")

  const sendgridKey = readlineSync.question('Sendgrid API key? ', { hideEchoBack: true })

  const certificate = await generate_x509()
  const hash = await writePassword()

  await Promise.all([
    createVolumeFile('volumes/dovecot.cer', certificate.certificate),
    createVolumeFile('volumes/dovecot.key', certificate.privateKey),
    createVolumeFile('volumes/dovecot_password_file', `me@k8s-mail.com:{ARGON2ID}${hash}:nobody:nogroup`),
    createVolumeFile('volumes/dovecot_submission_password_file', sendgridKey)
  ])

  const rawSource = await readFile('kubernetes.yml', 'utf8')
  let sourceDocs = yaml.loadAll(rawSource)
  let secretsData: any = {}
  const files = await readdir('volumes')
  for (const file of files) {
    secretsData[file] = await readFile(`volumes/${file}`, 'base64')
  }
  const secrets = { ...secretTemplate }
  secrets.data = secretsData

  sourceDocs.push(secrets)

  const sourceYaml = sourceDocs.flatMap((el: string) => yaml.dump(el)).join('---\n')

  createVolumeFile('kubernetes_with_secrets.yml', sourceYaml)

  console.info("done")
}

program()
