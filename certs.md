
# Listing a Keystore 
`keytool -list -keystore truststore.bks -storetype bks -storepass xxxxxxx`


# Convert PEM <-> P12 
```sh
(Cert)
openssl pkcs12 -clcerts -nokeys -in apns-cert.p12 -out apns-cert.pem
(Key)
openssl pkcs12 -nocerts -in apns-key.p12 -out apns-key.pem
```

# Remove encryption from key .pem file 
`openssl rsa -in apns-key.pem -out apns-key-noenc.pem`

# Merge certificate and key .pem file into one single .pem file:
`cat apns-cert.pem apns-key-noenc.pem > apns-prod.pem`

