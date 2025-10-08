{
  n=eval(getenv("n"));

  es=factorint(n)[,2];
  print(norml2(es)==#es);
}
