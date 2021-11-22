const { generateKeyPairSync } = require('crypto');

const { privateKey, publicKey } = generateKeyPairSync('rsa', {
    modulusLength: 2048, // length of your key in bits
    publicKeyEncoding: {
        type: 'spki',  // recommeded to be 'spki' by Node.js docs
        format: 'pem',
    },
    privateKeyEncoding: {
        type: 'pkcs8',  // recommeded to be 'pkcs8' by Node.js docs
        format: 'pem',
        // cipher: 'aes-256-cbc',    // optional
        // passphrase: 'top secret', // optional
    },
});

console.log(publicKey);
console.log(privateKey);
// RSA: Rivest-Shamir-Adleman
// PEM: Privacy Enhanced Mail

// export the keys generated to be used in asymmetric
module.exports = {
    privateKey, publicKey
}
