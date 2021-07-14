# Pre-read

Before using this tool, I _highly_ recommend reading through my blog posts:

1. [Configuring Kubernetes and NGINX Ingress for a mail server](https://corybuecker.com/post/configuring-kubernetes-and-nginx-ingress-for-a-mail-server)
1. [Setting up Network File System (NFS) on Kubernetes](https://corybuecker.com/post/setting-up-network-file-system-nfs-on-kubernetes)
1. [Setting up Dovecot for IMAP and email submission on Kubernetes (K8s)](https://corybuecker.com/post/setting-up-dovecot-for-imap-and-email-submission-on-kubernetes)
1. [Running a mail server in Kubernetes (K8s), tying it all together](https://corybuecker.com/post/running-a-mail-server-in-kubernetes-k8s-tying-it-all-together)

Dovecot and Postfix can be _dangerous_ if misconfigured. The risks run from open relaying, where a malicious party forwards spam through your mail server, to unauthorized access of your email. Be certain that you understand each setting and how it affects deliverablilty and security.

# Build Kubernetes configuration
1. Run `npm install`
1. Run `npm run build`
1. Answer the question about Sendgrid.
1. Run `kubectl apply -f kubernetes_with_secrets.yml`
