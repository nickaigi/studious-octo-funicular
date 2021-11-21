// the fact that a hashing function always returns the same value means
// that it is predictable. If a hacker obtains a database and the passwords
// are hashed, they can often just go to something like a Rainbow table
// that has a bunch of precomputed hashes and find a bunch of commonly used
// passwords.
//
// A salt is just a random value that is added to the password before it is
// hashed

const { scryptSync, randomBytes, timingSafeEqual } = require('crypto');

function signup(email, password){
    const salt = randomBytes(16).toString('hex');

    // provide scrypt witht he password, the salt, and provide a key length
    // recommended to be 64
    const hashedPassword = scryptSync(password, salt, 64);
    // we store the hash password along with the salt in the database
    // by just prepennding it to the existing password and separated by
    // a semi-colon
    const user = { email, password: `${salt}:${hashedPassword}` }
}

function login(email, password){
    const user = users.find(v => v.email === email);
    const [salt, key] = user.password.split(':');
    // we could just compare the strings here... but we are going to use
    // the timingSafeEqual function which can prevent timing attacks
    const hashedBuffer = scryptSync(password, salt, 64);
    //
    // timing attack: a hacker measures the amount of time it takes to
    // perform an operation to obtain information about the value
    //
    // timingSafeEqual helps prevent from such attacks
    const keyBuffer = Buffer.from(key, 'hex');
    const match = timingSafeEqual(hashedBuffer, keyBuffer);

    if (match){
        return 'login success!'
    } else {
        return 'login fail!'
    }
}
