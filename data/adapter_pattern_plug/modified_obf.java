interface _I {
    void _p(String _s);
}

class _X {
    void _v(String _f) {
        System.out.println(_f);
    }
}

class _A implements _I {
    private _X _z = new _X();

    public void _p(String _n) {
        _z._v(_n);
    }
}
