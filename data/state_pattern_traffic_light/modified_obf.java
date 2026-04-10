package data.state_pattern_traffic_light;

interface _S {
    void _h(_C _x);
}

class _R implements _S {
    public void _h(_C _x) {
        _x._s(new _G());
    }
}

class _G implements _S {
    public void _h(_C _x) {
        _x._s(new _R());
    }
}

class _C {
    private _S _k = new _R();

    void _s(_S _t) {
        this._k = _t;
    }

    void _q() {
        _k._h(this);
    }
}

public class modified_obf {
    public static void main(String[] _a) {
        _C _o = new _C();
        _o._q();
        _o._q();
    }
}