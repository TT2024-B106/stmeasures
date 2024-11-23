from pytest import fixture
from pytest import approx

from stmeasures.calculate.sad import SAD

@fixture(scope="module")
def sad():
    return SAD()

def test_lib(sad):
    """
    Test that the shared library is loaded correctly.
    """
    assert sad.lib is not None

def test_sad_distance(sad):
    """
    Test the SAD distance calculation between two trajectories.
    """

    r = [(19.574399,-99.073148),(19.57442,-99.073162),(19.574267,-99.073117),(19.57443,-99.073133),(19.574384,-99.073114),(19.574385,-99.073097),(19.574399,-99.07313),(19.57417,-99.073095),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574404,-99.073132),(19.574393,-99.07316),(19.574389,-99.073135),(19.574393,-99.073141),(19.574393,-99.073141),(19.574399,-99.073148),(19.574399,-99.073146),(19.57437,-99.073137),(19.574393,-99.073138),(19.574393,-99.073138),(19.574393,-99.073138),(19.574393,-99.073138),(19.574398,-99.073142),(19.574399,-99.073148),(19.574399,-99.073148),(19.574372,-99.073135),(19.574399,-99.073148),(19.574391,-99.073143),(19.574399,-99.073148),(19.574401,-99.07316),(19.574399,-99.073148),(19.574405,-99.07315),(19.574405,-99.07315),(19.574405,-99.07315),(19.574405,-99.07315),(19.574405,-99.07315),(19.574405,-99.07315),(19.574392,-99.073141),(19.574399,-99.073142),(19.574372,-99.073135),(19.574392,-99.073142),(19.574395,-99.073141),(19.574379,-99.073135),(19.574374,-99.073135),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574392,-99.073142),(19.574393,-99.073141),(19.574391,-99.073142),(19.57439,-99.073137),(19.574372,-99.073135),(19.574399,-99.073148),(19.574399,-99.073148),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574414,-99.073169),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574406,-99.073134),(19.574398,-99.073146),(19.574397,-99.073164),(19.57442,-99.073162),(19.574401,-99.073119),(19.574409,-99.073135),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.572502,-99.072235),(19.57231,-99.071382),(19.556332,-99.064277),(19.556259,-99.064264),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556317,-99.064293),(19.556314,-99.064292),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.55582,-99.064323),(19.55582,-99.064323),(19.55582,-99.064323),(19.55582,-99.064323),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.55582,-99.064323),(19.55582,-99.064323),(19.556604,-99.064561),(19.556604,-99.064561),(19.556056,-99.064309),(19.556056,-99.064309),(19.556056,-99.064309),(19.556056,-99.064309),(19.556056,-99.064309),(19.556056,-99.064309),(19.556056,-99.064309),(19.556056,-99.064309),(19.55582,-99.064323),(19.55582,-99.064323),(19.556344,-99.064291),(19.556344,-99.064291),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556323,-99.064271),(19.556323,-99.064271),(19.556332,-99.064277),(19.556332,-99.064277),(19.556295,-99.064257),(19.556295,-99.064257),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.55582,-99.064323),(19.55582,-99.064323),(19.55633,-99.064275),(19.55633,-99.064275),(19.556284,-99.064288),(19.556284,-99.064288),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556332,-99.064277),(19.556349,-99.06428),(19.556349,-99.06428),(19.556332,-99.064277),(19.556332,-99.064277),(19.556307,-99.064257),(19.556307,-99.064257),(19.556291,-99.064217),(19.556291,-99.064217),(19.574446,-99.073161),(19.574446,-99.073161),(19.574437,-99.073129),(19.574437,-99.073129),(19.574399,-99.073124),(19.574399,-99.073124),(19.574399,-99.07314),(19.574399,-99.07314),(19.574417,-99.073166),(19.574417,-99.073166),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574372,-99.073135),(19.574431,-99.073114),(19.574431,-99.073114),(19.57442,-99.073162),(19.57442,-99.073162),(19.574448,-99.073107),(19.574448,-99.073107),(19.574419,-99.07316),(19.574419,-99.07316),(19.574418,-99.073164),(19.574418,-99.073164),(19.57445,-99.073104),(19.57445,-99.073104),(19.574417,-99.07316),(19.574417,-99.07316),(19.574407,-99.073079),(19.574407,-99.073079),(19.574427,-99.073087),(19.574427,-99.073087),(19.574446,-99.073086),(19.574446,-99.073086),(19.574394,-99.073142),(19.574394,-99.073142),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.57442,-99.073162),(19.574419,-99.073166),(19.574419,-99.073166),(19.574419,-99.073166),(19.574419,-99.073166),(19.574419,-99.073166),(19.574419,-99.073166)]
    s = [(19.516853,-99.042481),(19.51686,-99.042479),(19.51686,-99.042479),(19.516853,-99.042481),(19.51686,-99.042479),(19.516853,-99.042481),(19.516853,-99.042481),(19.51686,-99.042479),(19.51686,-99.042479),(19.516853,-99.042481),(19.51686,-99.042479),(19.516853,-99.042481)]

    epsilon = 0.01
    expected_distance = 0.045033399

    assert sad.distance(r, s, epsilon) == approx(expected_distance)
