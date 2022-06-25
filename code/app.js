symbol = ['½', '∫', 'µ', '∆', '∴', 'ɣ', '²', '≈', '×', '÷', '℃', '℉', '±', '⅓', '¼', '∂', '∑', '√', '∇', '∛', '∜', '∞', '∝', '∬', '∲', '∯', '∊', 'ɳ', 'ɸ', '∠', '∩', '∪', 'θ', '³', 'ⁿ', 'ħ', 'ʋ', '$', '%', '!', 'α', 'β', 'λ', 'ψ', 'τ', 'ρ', 'π', '¼', 'Ω', 'χ', '₁', '₂', '₃', '₀', '-19', '$'];
SymbolName = ['1/2', 'integral', 'mu', 'delta', 'therefore', 'gamma', '^2', 'approx', 'multiply', 'divide', 'celsius', 'f', '+-', '1/3', '1/4', 'partial_diff', 'sigma', 'root', 'nabla', 'cube_root', '4th_root', 'infinite', 'proportional', 'double_integral', 'closed_integral', 'closed double integration', 'epsilon', 'eeta', 'phi', 'angle', 'intersection', 'union', 'theta', '^3', '^n', 'h bar', 'nu', 'dollar', 'percentage', 'factorial', 'alpha', 'beta', 'lambda', 'psi', 'tau', 'rho', 'pi', '1/4', 'omega b', 'chi b', ',1', ',2', ',3', ',0', '^-19', 'dollar']

symdict = {};

for (i = 0; i < symbol.length; i++) {
    symdict[SymbolName[i]] = symbol[i];
}



function ModifyInput() {

    text = document.getElementById('writingscreen');
    console.log(text.value);

    words = text.value.split(' ');
    console.log(words);
    console.log(symdict);

    for (i = 0; i < words.length; i++) {
        //console.log(SymbolName)
        //console.log(words[i])
        if (SymbolName.includes(words[i])) {
            if (words[i] != words[words.length - 1]) {
                words[i] = symdict[words[i]]
            }
        }
    }
    console.log(words);

    var FinalText = words.join(' ');

    console.log(FinalText);
    text.value = FinalText;

}