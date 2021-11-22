// often times we don't need to encrypt data, we just need to validate that
// it came from a trusted party
//
// What is a digital signature?
// The sender of the message will use their private key to sign a hash of the original message
// The private key guarantees authenticity
// The hash guarantees that the message can not be tampered with because it would produce an entirely different signature
// The recepient can then use the public key to validate the authenticity of the message

const { createSign, createVerify } = require('crypto');
const { publicKey, privateKey } = require('./keypair');

const message = 'this data must be signed';

const signer = createSign('rsa-sha256');  // use RSA + SHA

// Sign
signer.update(message);

const signature = signer.sign(privateKey, 'hex');

// Verify
const verifier = createVerify('rsa-sha256');
verifier.update(message);

const isVerified = verifier.verify(publicKey, signature, 'hex');
