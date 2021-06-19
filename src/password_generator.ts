import * as argon2 from 'argon2'
const { v4: uuidv4 } = require('uuid')

const writePassword = async (defaultPassword: string | undefined = undefined) => {
  const password: string = defaultPassword ?? uuidv4()

  console.info(`The password will not be shown again: ${password}`)

  const hash = await argon2.hash(password);

  return hash
}

export default writePassword
