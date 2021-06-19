import generate_x509 from './src/certificate'
import { chmod, writeFile, rm } from 'fs/promises'
import writePassword from './src/password_generator'
const readlineSync = require('readline-sync')

async function createVolumeFile(file: string, contents: string) {
  await rm(file)
  await writeFile(file, contents, { flag: 'w+' })
  chmod(file, 0o444)
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

  console.info("done")
}

program()
