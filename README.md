# amp

You are using Cisco AnyConnect Secure Mobility Client and want to use several profiles to access different VPN hosts. _amp_ (AnyConnect Multi Profile) utility helps you to manage your profiles using simpe CLI interface.

Simple utility which helps to manage Cisco Any Connect profiles

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

### Options

Available options from `Profile.xml` file
