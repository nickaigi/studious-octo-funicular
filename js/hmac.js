// HMAC
// Hash-Based Message Authentication Code
// simply defined as a hash that also requires a password
//
// The only person who can create the same hash signature must also have the
// corresponding password or key
// An example is a JSON web token for authentication on the web
// When a user logs in on a trusted server, it generates a token with its key,
// then the client and server can pass it back and forth and the server can
// trust it, because it knows that only someone with the secret key could generate
// that hash signature
const { createHmac } = require('crypto');

const key = 'super-secret';
const message = 'ghost_busters';

const hmac = createHmac('sha256', key).update(message).digest('hex');

console.log(hmac);

// we get the same hash when the same password is used.
// but if a different password is used, we get an entirely different hash

const key2 = 'other-password';

const hmac2 = createHmac('sha256', key2).update(message).digest('hex');

console.log(hmac2);
