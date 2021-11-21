// the fact that a hashing function always returns the same value means
// that it is predictable. If a hacker obtains a database and the passwords
// are hashed, they can often just go to something like a Rainbow table
// that has a bunch of precomputed hashes and find a bunch of commonly used
// passwords.
//
// A salt is just a random value that is added to the password before it is
// hashed

const { scryptSync, randomBytes } = require('crypto');

function signup(email, password){
    const salt = randomBytes(16).toString('hex');

    // provide scrypt witht he password, the salt, and provide a key length
    // recommended to be 64
    const hashedPassword = scryptSync(password, salt, 64);
    // we store the hash password along with the salt in the database
    const user = { email, password: `${salt}:${hashedPassword}` }
}

function login(email, password){
}
