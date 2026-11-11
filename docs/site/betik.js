(function () {
  var GORUNUMLER = ["basla", "yenilikler", "skiller", "istemler", "kurallar", "akislar", "dosyalar", "ipuclari", "destek"];
  var bolumler = document.querySelectorAll(".gorunum > section");
  var baglar = document.querySelectorAll(".menu a, a[data-git]");
  function goster() {
    var h = (location.hash || "").slice(1);
    var hedef = h, satir = null;
    if (GORUNUMLER.indexOf(h) === -1) {
      var el = h ? document.getElementById(h) : null;
      var ust = el ? el.closest(".gorunum > section") : null;
      hedef = ust ? ust.id.replace("g-", "") : "basla"; satir = el;
    }
    bolumler.forEach(function (b) { b.hidden = b.id !== "g-" + hedef; });
    document.querySelectorAll(".menu a").forEach(function (a) {
      if (a.getAttribute("href") === "#" + hedef) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    });
    if (satir) { if (satir.tagName === "DETAILS") satir.open = true; var d = satir.querySelector && satir.querySelector("details"); if (d) d.open = true; satir.scrollIntoView({block: "center"}); }
    else window.scrollTo(0, 0);
  }
  window.addEventListener("hashchange", goster);
  goster();
  document.querySelectorAll(".sekmeler").forEach(function (grup) {
    var hedef = document.getElementById(grup.dataset.hedef);
    grup.querySelectorAll("button").forEach(function (b) {
      b.addEventListener("click", function () {
        grup.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        hedef.querySelectorAll("[data-sekme]").forEach(function (k) { k.hidden = !(b.dataset.sekme === "hepsi" || k.dataset.sekme === b.dataset.sekme); });
        try { localStorage.setItem("sekme-" + grup.dataset.hedef, b.dataset.sekme); } catch (e) {}
      });
    });
    var kayit = null; try { kayit = localStorage.getItem("sekme-" + grup.dataset.hedef); } catch (e) {}
    var b0 = kayit && grup.querySelector('button[data-sekme="' + kayit + '"]'); if (b0) b0.click();
  });
  document.querySelectorAll(".kopyala").forEach(function (b) {
    b.addEventListener("click", function () {
      var kaynak = document.getElementById(b.dataset.hedef);
      var metin = kaynak.textContent;
      function tamam() { b.textContent = "Kopyalandı"; b.classList.add("oldu"); setTimeout(function () { b.textContent = "Kopyala"; b.classList.remove("oldu"); }, 1600); }
      function sec() { var r = document.createRange(); r.selectNodeContents(kaynak); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = "Seçildi, kopyalayın"; }
      try { navigator.clipboard.writeText(metin).then(tamam, sec); } catch (e) { sec(); }
    });
  });
})();
