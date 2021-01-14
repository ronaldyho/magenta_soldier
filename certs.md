
# READ
## Keystore 
`keytool -list -keystore truststore.bks -storetype bks -storepass xxxxxxx`

## PKCS12 
`openssl pkcs12 -info -in keystore.p12`

## x509 PEM
`openssl x509 -in mycert.pem -text -noout`

# Convert PEM <-> P12 
```sh
(Cert)
-clcerts      only output client certificates.
-cacerts      only output CA certificates.

$ openssl pkcs12 -clcerts -nokeys -in apns-cert.p12 -out apns-cert.pem
$ openssl pkcs12 -cacerts -nokeys -in tenant1_web_80_9 -out tenant1_web_80_9.pem

(Key)
$ openssl pkcs12 -nocerts -in apns-key.p12 -out apns-key.pem
```

# Remove encryption from key .pem file 
`openssl rsa -in apns-key.pem -out apns-key-noenc.pem`

# Merge certificate and key .pem file into one single .pem file:
`cat apns-cert.pem apns-key-noenc.pem > apns-prod.pem`

