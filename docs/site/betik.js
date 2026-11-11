(function () {
  var kartlar = Array.prototype.slice.call(document.querySelectorAll(".kart"));
  var dugmeler = Array.prototype.slice.call(document.querySelectorAll(".suzgec button"));
  var ara = document.getElementById("ara");
  var bos = document.getElementById("bos");
  var grup = "hepsi";
  function suz() {
    var q = (ara.value || "").toLocaleLowerCase("tr").trim();
    var gorunen = 0;
    kartlar.forEach(function (k) {
      var uygun = (grup === "hepsi" || k.dataset.grup === grup) && (!q || k.dataset.ara.indexOf(q) !== -1);
      k.hidden = !uygun;
      if (uygun) gorunen++;
    });
    bos.hidden = gorunen !== 0;
  }
  dugmeler.forEach(function (d) {
    d.addEventListener("click", function () {
      grup = d.dataset.grup;
      dugmeler.forEach(function (x) { x.classList.toggle("secili", x === d); x.setAttribute("aria-pressed", x === d ? "true" : "false"); });
      suz();
    });
  });
  ara.addEventListener("input", suz);
  document.querySelectorAll(".kopyala").forEach(function (b) {
    b.addEventListener("click", function () {
      var hedef = document.getElementById(b.dataset.hedef);
      var metin = hedef.textContent;
      function tamam() { b.textContent = "Kopyalandı"; setTimeout(function () { b.textContent = "Kopyala"; }, 1600); }
      function sec() { var r = document.createRange(); r.selectNodeContents(hedef); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = "Seçildi"; }
      try { navigator.clipboard.writeText(metin).then(tamam, sec); } catch (e) { sec(); }
    });
  });
  function hashKart() {
    var h = location.hash.slice(1);
    kartlar.forEach(function (k) { k.classList.toggle("vurgulu", k.id === h); });
    var k = document.getElementById(h);
    if (k && k.classList.contains("kart")) { k.hidden = false; var d = k.querySelector("details"); if (d) d.open = true; }
  }
  window.addEventListener("hashchange", hashKart);
  hashKart();
})();
