from app import App

def test_get_val():
  app = App()
  assert app.get_val() == 4
