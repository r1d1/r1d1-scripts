const canvas = document.getElementById('map_hex_canvas');
const ctx = canvas.getContext('2d');

// hex params
const a = 2 * Math.PI / 6;
const r = 50;


function init()
{
    draw_hex(r,r);
}

init();

function draw_hex(x,y)
{
    ctx.beginPath();

    for (let i = 0 ; i < 6 ; i++)
    {
        ctx.lineTo(x + r * Math.cos(a * i), y + r * Math.sin(a * i));
    }
    ctx.closePath();
    ctx.stroke();
}
