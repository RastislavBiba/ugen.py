import ugen
import mock

def secti(a, b):
    return a + b
def test_help():
    assert ugen.help() == "Here are instructions for you:\n"


def test_nickname():
   assert ugen.nickname("Milan","Rastislav","Stefanik") == "mrstefan"
   assert ugen.nickname("Jozef", "Miloslav", "Hurban")=="jmhurban"
   assert ugen.nickname("Jozef","", "Murgas") == "jmurgas"
   assert ugen.nickname("Pista","", "Hufnagel") == "phufnag"


def test_main():

  with mock.patch.object(ugen, "main", return_value=42):
    with mock.patch.object(ugen, "__name__", "__main__"):
      with mock.patch.object(ugen.sys,'exit') as mock_exit:
         ugen.main()

test_help()
test_nickname()
test_main()