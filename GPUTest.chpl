

inline proc indexAt(n: int,shape) {
    param rank = shape.size;
    var idx: rank * int;
    var order = n;
    var div = 1;
    for param i in 0..<rank do
        div *= shape(i);
    for param i in 0..<rank {
        div /= shape(i);
        idx(i) = order / div;
        order %= div;
    }
    return idx;
}



on here.gpus[0] {
    var D = {0..100,0..100};
    var A: [D] int;
    const shape = D.shape;
    forall i in 0..<D.size {
        const idx = indexAt(i,shape);
        A[idx] = i;
    }
    writeln(A);
}