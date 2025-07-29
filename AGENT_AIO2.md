### **AIO機能リファクタリング AIエージェント向け詳細指示書 v2**

**目標:** AIO\_Strengthening\_Plan\_20250730に基づき、AIO（生成AI検索適合性）のスコアリングロジックとUIを全面的にリファクタリングする。さらに、**URLの業種を判定し、パーソナライズされたコンテンツ提案を行うことで、ツールの付加価値を最大化する。**

**前提:**

* あなたは、提供されたファイル群にアクセスできるAIコーディングエージェントです。  
* 各フェーズの指示に従い、指定されたファイルを変更してください。  
* 変更は、既存のコードの構造とスタイルを尊重しつつ行ってください。

### **フェーズ 1: AIOスコア算出ロジックの基盤再構築**

(変更なし)  
このフェーズでは、古いスコア算出ロジックを廃止し、新しい評価軸の骨格を構築します。  
(指示内容は前バージョンと同じ)

### **フェーズ 2: 新規評価指標の実装**

(変更なし)  
このフェーズでは、core ディレクトリに新しいスコアリング用のファイルを作成し、各評価指標の具体的なロジックを実装します。  
(指示内容は前バージョンと同じ)

### **【新規】フェーズ 2.5: 業種判定とパーソナライズ機能の実装**

**目的:** ユーザーから提案された、ツールの核となる付加価値機能を実装する。サイトの業種を自動判定し、その業種に特有の「あるべきコンテンツ」の過不足を分析し、具体的な改善提案を行う。

**対象ファイル:** core/industry\_detector.py, core/aio\_scorer.py, seo\_aio\_streamlit.py

**手順:**

1. **core/industry\_detector.py の強化:**  
   * INDUSTRY\_KEYWORDS に加え、業種ごとに「推奨されるコンテンツのキーワード」を定義する新しい辞書 INDUSTRY\_CONTENTS を作成します。  
     INDUSTRY\_CONTENTS \= {  
         'restaurant': {'keywords': \['メニュー', 'コース', '予約', 'アクセス', '地図', 'テイクアウト', 'デリバリー'\], 'display\_name': '飲食店'},  
         'construction': {'keywords': \['施工事例', 'お客様の声', '技術紹介', '安全管理', '会社概要', '見積もり'\], 'display\_name': '建設業'},  
         'clinic': {'keywords': \['診療案内', '医師紹介', 'アクセス', '予約', '診療時間', '初診'\], 'display\_name': 'クリニック'},  
         \# 他の主要な業種も追加  
     }

   * detect\_industry 関数が、判定した業種のキー（例: restaurant）を返すようにします。  
2. **core/aio\_scorer.py への新機能追加:**  
   * 新しい関数 calculate\_personalization\_score(text, industry, industry\_contents\_map) を作成します。  
   * この関数は、判定された industry に基づき、industry\_contents\_map から推奨コンテンツのキーワードリストを取得します。  
   * text 内に、それらのキーワードがいくつ含まれているかを計算し、網羅率をスコア（0-100）として算出します。  
   * さらに、text 内に**含まれていなかった推奨キーワードのリスト**（例: \['予約', 'テイクアウト'\]）も返り値に含めます。  
3. **calculate\_aio\_score 関数の更新:**  
   * seo\_aio\_streamlit.py 内の calculate\_aio\_score を再度改修します。  
   * まず detect\_industry を呼び出して業種を判定します。  
   * 次に calculate\_personalization\_score を呼び出し、「業種適合性」スコアと「不足コンテンツリスト」を取得します。  
   * 全体のスコア辞書に '業種適合性' を追加します。  
     \# calculate\_aio\_score 内の処理イメージ  
     industry \= detect\_industry(text)  
     personalization\_score, missing\_contents \= calculate\_personalization\_score(text, industry, INDUSTRY\_CONTENTS)

     scores\['業種適合性'\] \= personalization\_score  
     \# ...  
     return total\_score, scores, industry, missing\_contents

### **フェーズ 3: レポートとUIの改修**

**目的:** 新しいスコアとパーソナライズされたアドバイスを、ユーザーに分かりやすく提示する。

**対象ファイル:** seo\_aio\_streamlit.py, core/visualization.py

**手順:**

1. **レーダーチャートの更新:**  
   * **core/visualization.py:** create\_aio\_radar\_chart が、新しい「業種適合性」を含む**6つの評価軸**に対応できるように改修します。  
2. **UIへのパーソナライズ結果表示:**  
   * **seo\_aio\_streamlit.py:**  
     * 分析後、まず判定結果を表示します。  
       industry\_display\_name \= INDUSTRY\_CONTENTS.get(industry, {}).get('display\_name', '特定できませんでした')  
       st.subheader(f"判定された業種: {industry\_display\_name}")

     * generate\_actionable\_advice を改修し、「不足コンテンツリスト」に基づいて具体的な提案を生成するロジックを追加します。  
       * **業種が特定できた場合:**「**建設業**のサイトとして、見込み客が求める『**施工事例**』や『**お客様の声**』に関する情報が不足しているようです。これらのコンテンツを追加することで、サイトの信頼性が向上し、受注機会の増加につながります。」  
       * **業種が特定できなかった場合:**「サイトのコンテンツが少ないため、業種を特定できませんでした。事業内容、サービス、会社情報などを具体的に記述し、コンテンツを充実させることを強くお勧めします。」  
     * これらのパーソナライズされたアドバイスを、レポートの一番目立つ場所に表示します。  
3. **PDFレポートの更新:**  
   * create\_pdf 関数を改修し、6軸になった新しいレーダーチャート、判定された業種、そしてパーソナライズされた具体的なアドバイスがPDFに含まれるようにします。

### **フェーズ 4: テストコードの更新と最終確認**

**手順:**

1. **新テストの作成:**  
   * tests ディレクトリに test\_personalization.py を作成するか、既存のテストファイルに追記します。  
   * calculate\_personalization\_score に対するテストを追加します。特定の業種のサンプルテキストと、期待されるスコア、不足コンテンツリストを検証します。  
   * detect\_industry のテストケースを拡充します。  
2. **総合テスト:**  
   * 様々な業種のWebサイトURL（飲食店、建設業、クリニック、士業など）を入力し、業種判定とアドバイスが適切に機能するかを重点的に確認します。  
   * コンテンツが極端に少ないサイトを入力し、「業種特定不可」のメッセージが正しく表示されることを確認します。