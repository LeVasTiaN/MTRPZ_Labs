const fs = require('fs');
const readline = require('readline');

function isNumeric(value) {
    return !isNaN(value) && isFinite(value);
}

function solveQuadratic(a, b, c) {
    console.log(`Equation is: ${a}x^2 + ${b}x + ${c} = 0\n`)
    const discriminant = b * b - 4 * a * c;
    if (discriminant > 0) {
        const root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        const root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
        console.log(`There are two roots: x1 = ${root1}, x2 = ${root2}`);
    } else if (discriminant === 0) {
        const root = -b / (2 * a);
        console.log(`There is one root: x = ${root}`);
    } else {
        console.log('No real roots exist.');
    }
}

function askNumber(rl, promptText, allowZero = true) {
    return new Promise((resolve) => {
        const ask = () => {
            rl.question(promptText, (input) => {
                const value = parseFloat(input);
                if (!isNumeric(value) || (!allowZero && value === 0)) {
                    console.log(
                        !isNumeric(value)
                            ? `Invalid input. Expected a valid real number, got ${input} instead.`
                            : 'Invalid input. "a" cannot be 0 in a quadratic equation.'
                    );
                    ask();
                } else {
                    resolve(value);
                }
            });
        };
        ask();
    });
}

async function interactiveMode() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const a = await askNumber(rl, 'Enter a: ', false);
    const b = await askNumber(rl, 'Enter b: ');
    const c = await askNumber(rl, 'Enter c: ');

    solveQuadratic(a, b, c);
    rl.close();
}

function nonInteractiveMode(filename) {
    try {
        if (!fs.existsSync(filename)) {
            console.error(`Error: File "${filename}" does not exist.`);
            process.exit(1);
        }

        const content = fs.readFileSync(filename, 'utf8').trim();
        const [aStr, bStr, cStr] = content.split(/\s+/);

        if (aStr === undefined || bStr === undefined || cStr === undefined) {
            console.error('Error: File must contain three numeric values.');
            process.exit(1);
        }

        const a = parseFloat(aStr);
        const b = parseFloat(bStr);
        const c = parseFloat(cStr);

        if (!isNumeric(a) || !isNumeric(b) || !isNumeric(c)) {
            console.error('Error: File contains non-numeric values.');
            process.exit(1);
        }

        if (a === 0) {
            console.error('Error: "a" cannot be 0 in a quadratic equation.');
            process.exit(1);
        }

        solveQuadratic(a, b, c);
    } catch (err) {
        console.error('Unexpected error while reading file:', err.message);
        process.exit(1);
    }
}


const args = process.argv.slice(2);

if (args.length === 0) {
    interactiveMode();
} else {
    nonInteractiveMode(args[0]);
}
