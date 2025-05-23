<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>簡単な計算機</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .calculator {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .calculator input {
            margin: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .calculator button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .calculator button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>簡単な計算機</h1>
        <form onsubmit="calculate(event)">
            <input type="number" id="num1" placeholder="数値1を入力" required>
            <input type="number" id="num2" placeholder="数値2を入力" required>
            <button type="submit">計算する</button>
        </form>
        <div class="result" id="result">結果がここに表示されます</div>
    </div>

    <script>
        // 計算する関数
        function calculate(event) {
            event.preventDefault(); // ページのリロードを防ぐ

            // ユーザーが入力した数値を取得
            var num1 = document.getElementById("num1").value;
            var num2 = document.getElementById("num2").value;

            // 2つの数値を足す
            var result = parseFloat(num1) + parseFloat(num2);

            // 結果を表示
            document.getElementById("result").innerHTML = "結果: " + result;
        }
    </script>
</body>
</html>
