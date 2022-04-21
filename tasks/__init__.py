from invoke import task

@task
def test(c):
    "Run all tests"
    import unittest
    test_suite = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(test_suite)
