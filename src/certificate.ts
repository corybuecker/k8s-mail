const forge = require('node-forge')

type KeyPair = {
  privateKey: object,
  publicKey: object
}

async function generate_rsa() {
  return new Promise<KeyPair>((resolve, reject) => {
    forge.pki.rsa.generateKeyPair({ bits: 2048, workers: -1 }, function (err: string, keypair: KeyPair) {
      if (err != null) {
        reject(err)
      }

      resolve(keypair)
    })
  })
}

async function generate_x509() {
  const keyPair = await generate_rsa()

  const cert = forge.pki.createCertificate();

  cert.publicKey = keyPair.publicKey;
  cert.serialNumber = '01';
  cert.validity.notBefore = new Date();
  cert.validity.notAfter = new Date();
  cert.validity.notAfter.setFullYear(cert.validity.notBefore.getFullYear() + 1);

  const attrs = [{
    name: 'commonName',
    value: 'k8s-mail.com'
  }, {
    name: 'countryName',
    value: 'US'
  }, {
    shortName: 'ST',
    value: 'Texas'
  }, {
    name: 'localityName',
    value: 'Austin'
  }, {
    name: 'organizationName',
    value: 'K8s Mail'
  }, {
    shortName: 'OU',
    value: 'self-signed'
  }];

  cert.setSubject(attrs);

  cert.setIssuer(attrs);

  cert.setExtensions([{
    name: 'basicConstraints',
    cA: true
  }, {
    name: 'keyUsage',
    keyCertSign: true,
    digitalSignature: true,
    nonRepudiation: true,
    keyEncipherment: true,
    dataEncipherment: true
  }, {
    name: 'extKeyUsage',
    serverAuth: true,
    clientAuth: true,
    codeSigning: true,
    emailProtection: true,
    timeStamping: true
  }, {
    name: 'nsCertType',
    client: true,
    server: true,
    email: true,
    objsign: true,
    sslCA: true,
    emailCA: true,
    objCA: true
  }, {
    name: 'subjectAltName',
    altNames: [{
      type: 6, // URI
      value: 'https://mail.k8s-mail.com'
    }, {
      type: 7, // IP
      ip: '127.0.0.1'
    }, {
      type: 6, // URI
      value: 'http://localhost'
    }]
  }, {
    name: 'subjectKeyIdentifier'
  }]);

  cert.sign(keyPair.privateKey);

  return {
    certificate: forge.pki.certificateToPem(cert),
    privateKey: forge.pki.privateKeyToPem(keyPair.privateKey),
  }

}

export default generate_x509
