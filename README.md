1. Run `gen_self_signed_certificates.sh`
1. Run `python3 volumes_to_secret.py > kubernetes_with_secrets.yml`
1. Run `kubectl apply -f kubernetes_with_secrets.yml`
