HTML内の似たような使われ方を繰り返しされているコード片を検出することでコンポーネント化の支援をするツールです。
例えば以下のようなファイルがあった場合

```html sample1.html
~~~~~
<header id="my-header" class="container">
  <a href="http://foobar.com/">
    <img src="img/icon.png">
  </a>
  <ul>
    <li>
      <a href="https://foobar.com/blog" target="_blank">
        <img src="img/blog.png" width="20" height="20">
      </a>
    </li>
    <li>
      <a href="https://foobar.com/photos" target="_blank">
        <img src="img/photos.png" width="20" height="20">
      </a>
    </li>
  </ul>
  <img src="img/taro.png" width="120" height="120" alt="アイコンです">
  <h1>山田太郎</h1>
  <p>UI/UXデザイナー見習いです</p>
</header>
~~~~~
```

```html sample2.html
~~~~~
<header id="my-header" class="container">
  <a href="http://foobar.com/">
    <img src="img/icon.png">
  </a>
  <ul>
    <li>
      <a href="https://foobar.com/blog" target="_blank">
        <img src="img/blog.png" width="20" height="20">
      </a>
    </li>
    <li>
      <a href="https://foobar.com/photos" target="_blank">
        <img src="img/photos.png" width="20" height="20">
      </a>
    </li>
  </ul>
  <img src="img/yuta.png" width="120" height="120" alt="アイコンです">
  <h1>田中雄太</h1>
  <p>UI/UXデザイナープロです</p>
</header>
~~~~~
```

liタグで囲まれている部分の構造は似通っているためコンポーネント化の候補として以下のようなコードを提案します。
```html
<li>
  <a href={param1} target="_blank">
    <img src={param2} width="20" height="20">
  </a>
</li>
```

またheader部分は中のプロフィールに関する部分以外は共通であるので以下のようなコードを提案します。
```html
<header id="my-header" class="container">
  <a href="http://foobar.com/">
    <img src="img/icon.png">
  </a>
  <ul>
    <li>
      <a href="https://foobar.com/blog" target="_blank">
        <img src="img/blog.png" width="20" height="20">
      </a>
    </li>
    <li>
      <a href="https://foobar.com/photos" target="_blank">
        <img src="img/photos.png" width="20" height="20">
      </a>
    </li>
  </ul>
  {child1}
</header>
```