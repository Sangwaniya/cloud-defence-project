# cloud-defence-project
Detect and block suspicious outbound connections from pods running in your cluster using eBPF. Your mission includes monitoring activity, tracing processes, and implementing firewall-like controls using custom eBPF logic.

## setup
- git clone `https://github.com/Sangwaniya/cyber-defence-project.git`
- `sudo apt install python  docker code minikube kubectl` 
- setup local machine to use [gpg keys](https://docs.gitlab.com/user/ssh/#generate-an-ssh-key-pair) to avoid logging in every time commit is made 

- give exec priv to `build-image.sh`
    - `chmod +x build-images.sh`

## TODO
- [ ] dockerize all services(1/3)
- [ ] dockerize the .py file to app container
- [ ] find a way to store the container artifacts locally
- [ ] pull the local artifacts in the minikube cluster we have
- [ ] further steps for pod monitoring and blocking.
