#####################################################
#
# hashutils
#
# A handful of hashing utility functions
# to help us encrypt and decrypt sensitive user info
#
#####################################################

import random, string, hashlib, hmac

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = ''.join(random.choice(string.letters) for x in xrange(5))

    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    test_hash = make_pw_hash(name, pw, salt)
    return h == test_hash

SECRET = 'czUv86iAN9GXA3MT'
def hash_str(s):
    return hmac.new(SECRET,s).hexdigest()

def make_secure_val(s):
    return '%s|%s' % (s, hash_str(s))

def check_secure_val(h):
    s = h.split('|')[0]
    if h == make_secure_val(s):
        return s
