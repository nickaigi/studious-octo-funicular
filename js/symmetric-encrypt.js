// What happens when you want to share a secret with someone and also allow
// them to read the original message ?
// Enter Encryption
// 
// In symmetric encryption, there is a shared password that both the sender
// and receiver of the message will need.
const { createCipheriv, randomBytes, createDecipheriv } = require('crypto');

// iv : Initialization Vector

const message = "cry 'havoc', and let slip the dogs of war";
const key = randomBytes(32);
const iv = randomBytes(16);

// Initialization vector: prevent identical sequences of text
const cipher = createCipheriv('aes256', key, iv);
// pass the encryption algorithm
// AES: Advanced Encryption Standard AES

// encrypt
const encryptedMessage = cipher.update(message, 'utf8', 'hex')
    + cipher.final('hex');
// after calling final, the cipher can no longer be used to encrypt data
console.log(encryptedMessage);

// decrypt
const decipher = createDecipheriv('aes256', key, iv);
const decryptedMessage = decipher.update(encryptedMessage, 'hex', 'utf-8')
    + decipher.final('utf-8');
console.log(decryptedMessage);


// there is a big limitation to symmetric encryption: the sender and receiver
// need to share a password
