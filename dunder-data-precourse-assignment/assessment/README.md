# Precourse Assessment

This folder contains a test of the material covered throughout the precourse.

### Getting Started

Open the file `assessment.py` in your favorite text editor ([Visual Studio Code][1] is a popular choice). This file contains many functions that need to be completed. They currently use the keyword `pass` as a placeholder. Delete it and write the body of the function.

### Checking Correctness

To check your solutions you will run the file `assessment_unittest.py` from the command line.

```bash
$ pytest assessment_unittest.py
```

### Assessment output

After running the above command, you will get a message informing you of your performance. If any of the functions produced an incorrect result you will see:

```
 =========== m failed, n passed in x seconds ==================
 ```

 where m is the number of failures and n is number passed. If your code has an error in it, then tests won't be able to run. You will get a message about an error interrupting the tests. You'll need to fix your code so that it is executable before the tests can complete.

 The output also tells you which functions are failing the test. Look back up to see the exact names of the functions that are failing. Correct functions produce no output.

 When all functions return the correct answer, the output will be green.

### More on unit testing

 This test uses the [`pytest`][2] third-party library. See [test driven development][3] for more on testing.

[1]: https://code.visualstudio.com/
[2]: https://docs.pytest.org/en/latest/getting-started.html
[3]: https://en.wikipedia.org/wiki/Test-driven_development