var stringShift = function(s, shift) {
    var move = 0,
        s= s.split('');
    
    for (var i = 0; i < shift.length; i ++) {
        if (shift[i][0] === 0) {
            move -= shift[i][1];
        } else if (shift[i][0] === 1) {
            move += shift[i][1];
        }
    }
    
    if (move === 0 || move % s.length === 0) return s.join('');
    else if (move < 0) {
        // left
        let moves = (move * -1) % s.length;
        
        for (var i = 0; i < moves; i ++) {
            var letter = s.shift();
            s.push(letter);
        }
        
    } else if (move > 0) {
        // right
        let moves = (move) % s.length;
        
        for (var i = 0; i < moves; i ++) {
            var letter = s.pop();
            s.unshift(letter);
        }
    }
    
    return s.join('');
};