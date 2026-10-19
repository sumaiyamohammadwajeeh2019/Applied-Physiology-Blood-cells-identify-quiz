/* worker.js - alias/compat shim: some hosts block sw.js, so we keep worker.js identical.
   Register either file; both work. */
const CACHE = "blood-puzzle-v1";
const ASSETS = [
  "./",
  "./index.html",
  "./manifest.json",
  "./manifest.webmanifest",
  "./privacy.html",
  "./terms.html",
  "./10cells.jpg",
  "./real1.webp",
  "./real2.webp",
  "./real3.webp",
  "./real4.webp",
  "./real5.webp",
  "./real6.webp",
  "./real7.webp",
  "./real8.webp",
  "./real9.webp",
  "./real10.webp",
  "./icon-192.png",
  "./icon-512.png"
];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (e) => {
  if (e.request.method !== "GET") return;
  e.respondWith(
    caches.match(e.request, { ignoreSearch: true }).then((hit) => {
      if (hit) return hit;
      return fetch(e.request).then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(e.request, copy)).catch(() => {});
        return res;
      }).catch(() => caches.match("./index.html"));
    })
  );
});
