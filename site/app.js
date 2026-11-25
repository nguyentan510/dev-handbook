{
const H = window.HANDBOOK;
const TYPE = {overview:"Tổng quan",roadmap:"Lộ trình",tutorial:"Hướng dẫn học","how-to":"Cách làm",reference:"Tra cứu",explanation:"Giải thích",template:"Mẫu",decision:"Quyết định"};
const STATUS = {done:"Hoàn thành",draft:"Nháp",skeleton:"Khung"};
const $ = id => document.getElementById(id);
const root = document.documentElement;
const host = root.getAttribute("data-host-theme") || "";
const order = [];
const groupOf = {};
H.nav.forEach(g => g.items.forEach(id => { order.push(id); groupOf[id] = g.group; }));
const esc = s => String(s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const norm = s => s.normalize("NFD").replace(/[̀-ͯ]/g,"").replace(/đ/g,"d").replace(/Đ/g,"D").toLowerCase();

$("ver").textContent = "Dựng ngày " + H.built.split("-").reverse().join("/");

/* ---------- theme ---------- */
function isDark(){
  const t = root.getAttribute("data-theme");
  if (t) return t === "dark";
  return window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches;
}
function savedTheme(){ try { const t = localStorage.getItem("dh-theme"); return t === "light" || t === "dark" ? t : "auto"; } catch(e){ return "auto"; } }
function applyTheme(t, rerender){
  if (t === "auto") { if (host) root.setAttribute("data-theme", host); else root.removeAttribute("data-theme"); }
  else root.setAttribute("data-theme", t);
  try { localStorage.setItem("dh-theme", t); } catch(e) {}
  ["light","dark","auto"].forEach(k => $("th-"+k).setAttribute("aria-pressed", k === t ? "true" : "false"));
  if (rerender) { renderMermaid(); swapPictures(); }
}
["light","dark","auto"].forEach(k => $("th-"+k).addEventListener("click", () => applyTheme(k, true)));
applyTheme(savedTheme(), false);

/* ---------- nav ---------- */
function drawNav(q){
  const nq = norm(q || "");
  $("nav").innerHTML = H.nav.map(g => {
    const links = g.items.filter(id => !nq || norm(H.pages[id].title).includes(nq)).map(id => {
      const p = H.pages[id];
      const sub = /\/l2\/(?!README)/.test(p.path) ? " sub" : "";
      const tag = p.status === "skeleton" ? "<i>khung</i>" : p.status === "draft" ? "<i>nháp</i>" : "";
      return `<a href="#${id}" data-id="${id}" class="${sub.trim()}"><span>${esc(p.title)}</span>${tag}</a>`;
    }).join("");
    return links ? `<div class="ng"><h2>${esc(g.group)}</h2>${links}</div>` : "";
  }).join("") || '<p class="wcount">Không có trang phù hợp.</p>';
  markNav();
}
function markNav(){
  const id = current();
  document.querySelectorAll("#nav a").forEach(a => a.classList.toggle("cur", a.dataset.id === id));
}
$("nav-q").addEventListener("input", e => drawNav(e.target.value));
function setNav(open){
  document.body.classList.toggle("nav-open", open);
  $("menu-btn").setAttribute("aria-expanded", open ? "true" : "false");
}
$("menu-btn").addEventListener("click", () => setNav(!document.body.classList.contains("nav-open")));
$("scrim").addEventListener("click", () => setNav(false));

/* ---------- router ---------- */
function current(){
  const h = decodeURIComponent(location.hash.slice(1));
  return H.pages[h] ? h : "trang-chu";
}
let stepObs = null;
function render(){
  const id = current(), p = H.pages[id];
  const doc = $("doc");
  doc.innerHTML = p.html;
  document.title = p.title + " · dev-handbook";
  const h1 = doc.querySelector("h1");
  const meta = document.createElement("div");
  meta.className = "meta";
  meta.innerHTML = `<span class="badge t">${TYPE[p.type] || p.type}</span><span class="badge">${p.level === "chung" ? "Mọi cấp" : p.level}</span>` +
    `<span class="badge ${p.status}">${STATUS[p.status] || p.status}</span><span>Cập nhật ${p.updated.split("-").reverse().join("/")}</span><span>Xem lại ${p.review_by.split("-").reverse().join("/")}</span>`;
  if (h1) {
    h1.after(meta);
    const crumb = document.createElement("div");
    crumb.className = "crumb";
    crumb.textContent = groupOf[id];
    h1.before(crumb);
  }
  doc.querySelectorAll("table").forEach(t => {
    const w = document.createElement("div"); w.className = "tw"; t.before(w); w.appendChild(t);
    const heads = [...t.querySelectorAll("thead th")].map(th => th.textContent.trim());
    if (heads.length >= 4) {
      w.classList.add("stack");
      t.querySelectorAll("tbody tr").forEach(r => [...r.cells].forEach((c, i) => { if (heads[i]) c.dataset.l = heads[i]; }));
    }
  });
  doc.querySelectorAll("a[href^='http']").forEach(a => { a.target = "_blank"; a.rel = "noopener"; });
  codeBlocks(doc);
  const i = order.indexOf(id), prev = order[i-1], next = order[i+1];
  $("pager").innerHTML =
    (prev ? `<a href="#${prev}"><small>Trang trước</small>${esc(H.pages[prev].title)}</a>` : "") +
    (next ? `<a class="next" href="#${next}"><small>Trang sau</small>${esc(H.pages[next].title)}</a>` : "");
  $("src").innerHTML = `Nguồn: <code>${esc(p.path)}</code> · Phụ trách: ${esc(p.owner)}`;
  if (stepObs) { stepObs.disconnect(); stepObs = null; }
  $("main").classList.remove("with-panel");
  $("panel").innerHTML = "";
  doc.querySelectorAll("[data-widget]").forEach(w => {
    const k = w.dataset.widget;
    if (k === "flow-map") flowMap(w, doc);
    if (k === "glossary") glossary(w);
    if (k === "criteria") criteria(w);
  });
  swapPictures();
  renderMermaid();
  markNav();
  setNav(false);
}
window.addEventListener("hashchange", () => { render(); window.scrollTo(0, 0); });

/* ---------- pictures: follow the chosen theme ---------- */
function swapPictures(){
  document.querySelectorAll("#doc picture").forEach(pic => {
    const img = pic.querySelector("img");
    if (!img) return;
    pic.querySelectorAll("source").forEach(s => s.remove());
    img.src = img.getAttribute("src").replace(/-(light|dark)\.svg$/, isDark() ? "-dark.svg" : "-light.svg");
  });
}

/* ---------- code: copy + mermaid ---------- */
function codeBlocks(doc){
  doc.querySelectorAll("pre > code").forEach(code => {
    const pre = code.parentNode;
    if (code.className.includes("language-mermaid")) {
      const box = document.createElement("div");
      box.className = "mm";
      box.dataset.src = code.textContent;
      pre.replaceWith(box);
      return;
    }
    const wrap = document.createElement("div");
    wrap.className = "codebox";
    pre.before(wrap); wrap.appendChild(pre);
    const b = document.createElement("button");
    b.type = "button"; b.className = "copy"; b.textContent = "Sao chép";
    b.addEventListener("click", () => {
      const done = ok => { b.textContent = ok ? "Đã chép" : "Bôi đen để chép"; setTimeout(() => b.textContent = "Sao chép", 1600); };
      try {
        navigator.clipboard.writeText(code.textContent).then(() => done(true), () => { selectText(code); done(false); });
      } catch(e) { selectText(code); done(false); }
    });
    wrap.appendChild(b);
  });
}
function selectText(el){ const r = document.createRange(); r.selectNodeContents(el); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }
let mmCount = 0;
function renderMermaid(){
  const boxes = document.querySelectorAll(".mm");
  if (!boxes.length) return;
  const m = window.mermaid;
  if (!m) {
    boxes.forEach(b => { if (!b.dataset.done) b.innerHTML = `<p class="note">Sơ đồ đang tải. Nếu không hiện, đây là mã nguồn của sơ đồ:</p><pre><code>${esc(b.dataset.src)}</code></pre>`; });
    return;
  }
  try {
    m.initialize({startOnLoad:false, securityLevel:"strict", theme: isDark() ? "dark" : "neutral",
      fontFamily:'"Be Vietnam Pro", system-ui, sans-serif', themeVariables:{fontSize:"14px"}});
  } catch(e) {}
  boxes.forEach(b => {
    const id = "mm" + (++mmCount);
    m.render(id, b.dataset.src).then(r => { b.innerHTML = r.svg; b.dataset.done = "1"; })
     .catch(() => { b.innerHTML = `<p class="note">Không vẽ được sơ đồ, mã nguồn:</p><pre><code>${esc(b.dataset.src)}</code></pre>`; });
  });
}
const mjs = $("mermaid-js");
if (mjs) mjs.addEventListener("load", renderMermaid);
if (window.matchMedia) matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => { if (savedTheme() === "auto") renderMermaid(); });

/* ---------- widget: flow map ---------- */
const LAYERS = ["UI","API","Service","Job nền","Repository","Database"];
const MODS = ["Catalog","Order","Payment","Auth","Notify"];
const CELLS = {
"UI|Catalog":"Trang sản phẩm, giỏ hàng","UI|Order":"Nút đặt hàng, trạng thái đơn","UI|Payment":"Chuyển sang cổng, trang kết quả","UI|Auth":"Đăng nhập (tùy chọn)",
"API|Catalog":"GET /products","API|Order":"POST /orders","API|Payment":"Webhook từ cổng","API|Auth":"Middleware xác thực",
"Service|Catalog":"Giữ, nhả tồn kho","Service|Order":"Tính tiền, voucher","Service|Payment":"State machine, gọi cổng","Service|Auth":"Quyền sở hữu đơn","Service|Notify":"Soạn email",
"Job nền|Catalog":"Nhả hàng đơn hết hạn","Job nền|Payment":"Đối soát","Job nền|Notify":"Gửi từ outbox",
"Repository|Catalog":"Cập nhật tồn có điều kiện","Repository|Order":"Lưu đơn, món hàng","Repository|Payment":"Lưu thanh toán, webhook","Repository|Auth":"Tìm user","Repository|Notify":"Ghi, đọc outbox",
"Database|Catalog":"products, inventory","Database|Order":"orders, order_items","Database|Payment":"payments, webhook_events","Database|Auth":"users","Database|Notify":"outbox"};
function flowMap(w, doc){
  const steps = [];
  doc.querySelectorAll("h3").forEach(h => {
    const m = h.textContent.match(/^(\d+)\.\s*(.*)$/);
    if (!m) return;
    let ul = h.nextElementSibling;
    while (ul && ul.tagName !== "UL" && ul.tagName !== "H3") ul = ul.nextElementSibling;
    if (!ul || ul.tagName !== "UL") return;
    let cells = [], risk = "low";
    ul.querySelectorAll("li").forEach(li => {
      const t = li.textContent;
      if (t.startsWith("Ô trên bản đồ:")) cells = t.split(":")[1].split(",").map(s => s.trim().replace("/", "|")).filter(k => CELLS[k] !== undefined || k.includes("|"));
      if (t.startsWith("Rủi ro:")) { const r = t.split(":")[1]; risk = /cao/.test(r) ? "high" : /vừa/.test(r) ? "mid" : "low"; }
    });
    h.classList.add("step", "r-" + risk);
    steps.push({n:+m[1], title:m[2], cells, h});
  });
  const touch = {};
  steps.forEach(s => s.cells.forEach(k => (touch[k] = touch[k] || []).push(s.n)));
  const box = document.createElement("div");
  box.className = "fmap";
  w.replaceWith(box);
  if (matchMedia("(min-width: 1280px)").matches) { $("main").classList.add("with-panel"); $("panel").appendChild(box); }
  else { doc.querySelector("h2") ? doc.querySelector("h2").before(box) : null; }
  let cur = 1;
  function draw(){
    const s = steps.find(x => x.n === cur);
    const on = s ? s.cells : [];
    let h = '<h2>Bản đồ layer × module</h2><div class="fscroll"><div class="grid"><div></div>' + MODS.map(m => `<div class="gh">${m}</div>`).join("");
    LAYERS.forEach(l => {
      h += `<div class="gh r">${l}</div>`;
      MODS.forEach(m => {
        const k = l + "|" + m, ns = touch[k] || [];
        const nums = ns.map(n => `<b class="${n === cur ? "cur" : ""}">${n}</b>`).join("");
        h += `<button type="button" class="gc${on.includes(k) ? " on" : ""}" data-k="${k}"${ns.length ? "" : " disabled"} aria-label="${l}, ${m}">${nums ? `<span class="n">${nums}</span>` : ""}${CELLS[k] || ""}</button>`;
      });
    });
    h += `</div></div><p class="fcap">${s ? `Đang xem bước <b>${s.n}. ${esc(s.title)}</b>` : ""}${s && !s.cells.length ? " · cắt ngang mọi ô" : ""}. Bấm vào một ô để tới bước đầu tiên đi qua ô đó.</p>`;
    box.innerHTML = h;
    box.querySelectorAll(".gc[data-k]").forEach(b => b.addEventListener("click", () => {
      const ns = touch[b.dataset.k]; if (!ns) return;
      const next = ns.find(n => n > cur) || ns[0];
      const st = steps.find(x => x.n === next);
      cur = next; draw(); mark();
      st.h.scrollIntoView({behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block:"start"});
    }));
  }
  function mark(){ steps.forEach(s => s.h.classList.toggle("now", s.n === cur)); }
  draw(); mark();
  if ("IntersectionObserver" in window) {
    stepObs = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { const s = steps.find(x => x.h === e.target); if (s && s.n !== cur) { cur = s.n; draw(); mark(); } }
    }), {rootMargin:"-20% 0px -65% 0px"});
    steps.forEach(s => stepObs.observe(s.h));
  }
}

/* ---------- widget: glossary ---------- */
function glossary(w){
  const tw = w.nextElementSibling && w.nextElementSibling.classList.contains("tw") ? w.nextElementSibling : null;
  if (!tw) return;
  const rows = [...tw.querySelectorAll("tbody tr")];
  const groups = [...new Set(rows.map(r => r.cells[2].textContent))];
  let cat = "";
  w.innerHTML = `<div class="wtools"><input class="wq" id="gq" type="search" placeholder="Tìm, ví dụ: idempotency, quay lui, mvp" aria-label="Tìm thuật ngữ" autocomplete="off"></div><div class="wtools" id="gchips"></div><p class="wcount" id="gcount"></p>`;
  function chips(){
    $("gchips").innerHTML = [["", "Tất cả"]].concat(groups.map(g => [g, g])).map(([k, l]) =>
      `<button type="button" class="chip" data-k="${esc(k)}" aria-pressed="${k === cat}">${esc(l)}</button>`).join("");
    $("gchips").querySelectorAll(".chip").forEach(b => b.addEventListener("click", () => { cat = b.dataset.k; chips(); filter(); }));
  }
  function filter(){
    const q = norm($("gq").value.trim());
    let n = 0;
    rows.forEach(r => {
      const ok = (!cat || r.cells[2].textContent === cat) && (!q || norm(r.textContent).includes(q));
      r.hidden = !ok; if (ok) n++;
    });
    $("gcount").textContent = `Hiển thị ${n}/${rows.length} thuật ngữ`;
  }
  $("gq").addEventListener("input", filter);
  chips(); filter();
}

/* ---------- widget: criteria ---------- */
function criteria(w){
  const tw = w.nextElementSibling && w.nextElementSibling.classList.contains("tw") ? w.nextElementSibling : null;
  if (!tw) return;
  const th = document.createElement("th"); th.textContent = "Bạn đạt?";
  tw.querySelector("thead tr").prepend(th);
  const rows = [...tw.querySelectorAll("tbody tr")];
  rows.forEach((r, i) => {
    const td = document.createElement("td");
    td.innerHTML = `<label><input type="checkbox" id="cr${i}"><span class="lbl">Kế hoạch của tôi đạt tiêu chí này</span></label>`;
    r.prepend(td);
  });
  w.innerHTML = `<div class="score"><b id="sct"></b><div class="bar"><i id="scb"></i></div><small id="scm"></small></div>`;
  function score(){
    const n = rows.filter((_, i) => $("cr"+i).checked).length;
    $("sct").textContent = `Kế hoạch của bạn: ${n}/${rows.length}`;
    $("scb").style.width = (n / rows.length * 100) + "%";
    $("scm").textContent = n === 0 ? "Tick những tiêu chí kế hoạch của bạn đã đạt. Điểm không được lưu."
      : n < 4 ? "Còn thiếu nhiều. Bắt đầu từ mục tiêu, phạm vi và ưu tiên."
      : n < 7 ? "Khá ổn. Bổ sung phần còn thiếu, nhất là rủi ro và tiêu chí hoàn thành."
      : "Kế hoạch khá chắc. Giữ lịch rà soát để cập nhật khi thực tế lệch.";
  }
  rows.forEach((_, i) => $("cr"+i).addEventListener("change", score));
  score();
}

drawNav("");
render();
}
