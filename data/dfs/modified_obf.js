function f(g, s) {
    const v = new Set();
    const r = [];
    function ex(c) {
        v.add(c); r.push(c);
        for (const n of (g[c] || []))
            if (!v.has(n)) ex(n);
    }
    ex(s);
    return r;
}

const g = { 0:[1,2], 1:[0,3,4], 2:[0,5], 3:[1], 4:[1], 5:[2] };
console.log(f(g, 0));
