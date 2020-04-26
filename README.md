# amp

If you use Cisco AnyConnect Secure Mobility Client `amp` utility might help you to initialize you AnyConnect profile, manage your server list, etc. It has simple CLI and easy to use.

## Commands

### Init

`init` command helps to initialize `Profile.xml` file with profiles if not exists

### Host

You can use this command to list, add and update hosts in your Cisco AnyConnect profile.

To list available server which you can you to connect, type:

```shell
python3 amp.py host ls
```

or just:

```shell
python3 amp.py host
```

### Add

`add` command helps add new profiles to the `Profile.xml` config file

### Update

`update` command helps to update existing profile

### Delete

`delete` command helps to delete existing profile if you dont need it

### Schema

`schema` command show XSD schema where you can find which options can be used to configure your Cisco AnyConnect profile.
