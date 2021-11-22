// used in HTTPS web traffic
// browser finds public key of a SSL certificate installed on the website
// that public key is used to encrypt any data that you send to the website
// preventing hackers from gaining any useful infor in transit
// Your data is then decrypted using the private key by the trusted website
const { publicEncrypt, privateDecrypt } = require('crypto');
const { publicKey, privateKey } = require('./keypair');

const message = "cry 'havoc' and let slip the dogs of war";

const encryptedData = publicEncrypt(
    publicKey,
    Buffer.from(message) // recall mailbox analogy, this would be the message
);


console.log(encryptedData.toString('hex'));


const decryptedData = privateDecrypt( // unlock the mailbox
    privateKey,
    encryptedData
);


console.log(decryptedData.toString('utf-8'));
