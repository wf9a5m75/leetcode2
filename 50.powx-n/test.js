
const addBinary = (a, b) => {
  // (01)与えられた2つの2進数文字列を、合計して2進数で返す
  // (02)10進数に直したりはせずに、2進数のまま処理
  /* (03)一桁ずつの数字の組み合わせは以下①〜④の4パターン。
            ① ② ③ ④
    a       0 　1　 0　 1
    b       0 　0 　1　 1
  */

  // (04)上記④のケースは桁が一つ増えるので要考慮。桁が上がったか判定するための変数を用意しておく。
  let carry = 0; //桁上げ判定用
  let loStrProc = ""; //a,bのうち長い方を加工
  let shStrProc = ""; //a,bのうち短い方を加工
  let Answer ="";
  let tail =0;

  // (04)aとbで長さが違う場合もある。出力結果がどのパターンでもおさまるように、長い方＋1桁を想定しておく
  //このブロックの処理で、どちらの値も長い方の桁数＋1の形式に統一する
  let maxLength = 0;
  if(a.length >= b.length){
    maxLength =a.length;
    loStrProc = "" + "0" +a;
    shStrProc = "" + "0".repeat(Math.abs(a.length - b.length)+1) + b;
  }else{
    maxLength =b.length;
    loStrProc = "" + "0" +b;
    shStrProc = "" + "0".repeat(Math.abs(b.length - a.length)+1) + a;
  }
  console.log(loStrProc);
  console.log(shStrProc);

  // (05)ここから、aとbの加算（末尾の桁から）、桁上げ処理
  /*for (let i = 0; i < 9; i++) {
    str = str + i;
  }*/

  for (let i = 0; i < maxLength; i++) {
    tail = carry +Number(loStrProc.substr(-1,1))+Number(shStrProc.substr(-1,1));
    if (tail % 2 > 0){  //奇数なら
      Answer = "" + "1" + Answer;
    }else{//偶数なら
      Answer = "" + "0" + Answer;
    }
  }

    if ((loStrProc.substr(-1,1) =="1") && (shStrProc.substr(-1,1) =="1")) {
      carry =1;
    }

  console.log ("答え" + Answer);

    return "";
};

console.log(addBinary("10", "1"))
