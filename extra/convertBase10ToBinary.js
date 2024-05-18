const convertBase10ToBinary = (int, base = 2) => {
  if (int === 0) return 0;

  let result = "";
  while (int > 0) {
    const remainder = int % base;
    const quotient = Math.floor(int / base);
    result = `${remainder}${result}`;

    int = quotient;
  }
  return result;
};
