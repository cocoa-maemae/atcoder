const main = args => {
  let [[A, B, C], [K]] = args.trim().split('\n').map(r=>r.split` `.map(v=>v|0))
  let cnt = 0
  while (A>=B) {
    B *= 2
    cnt++
  }
  while (B>=C) {
    C *= 2
    cnt++
  }
  console.log(cnt > K ? 'No' : 'Yes')
}
main(require('fs').readFileSync('/dev/stdin', 'utf-8'))
