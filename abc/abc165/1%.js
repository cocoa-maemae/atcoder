const main = arg => {
  const X = Number(arg);
  let deposit = 100n;
  let year = 0;
  while (deposit < X) {
    deposit += deposit / 100n;
    year++;
  }
  console.log(year);
}
main(require('fs').readFileSync('/dev/stdin', 'utf-8'));
