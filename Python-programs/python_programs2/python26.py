Str = "this is simple string....!!!";
Str = Str.encode('base64','strict');
print "The Encoded String: " + Str
print "The Decoded String: " + Str.decode('base64','strict')
