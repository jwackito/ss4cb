function f(g, s) {
    const v = new Set();
    const q = [];
    const r = [];
    v.add(s);
    q.push(s);
    while (q.length > 0) {
        const c = q.shift();
        r.push(c);
        for (const n of (g[c] || [])) {
            if (!v.has(n)) { v.add(n); q.push(n); }
        }
    }
    return r;
}

const g = { 0:[1,2], 1:[0,3,4], 2:[0,5], 3:[1], 4:[1], 5:[2] };
console.log(f(g, 0));
