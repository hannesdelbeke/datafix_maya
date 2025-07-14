from datafix.core import Adapter
from datafix_maya.types import Material
from datafix_maya.types import ShaderfxGameHair, ShaderfxShader, StingrayPBS, Anisotropic, Blinn, Brownian, Bulge, Checker, Cloth, Cloud, Crater, EnvBall, EnvChrome, EnvCube, EnvFog, EnvSky, EnvSphere, File, Fractal, Granite, Grid, HairTubeShader, Lambert, LayeredShader, LayeredTexture, Leather, LightFog, Mandelbrot, Mandelbrot3D, Marble, Mountain, Movie, Noise, Ocean, OceanShader, ParticleCloud, ParticleSamplerInfo, Phong, PhongE, Projection, PsdFileTex, Ramp, RampShader, Rock, ShadingMap, Snow, SolidFractal, StandardSurface, Stencil, Stucco, UseBackground, VolumeFog, VolumeNoise, Water, Wood


class MaterialAdapter(Adapter):
    input_types = [ShaderfxGameHair, ShaderfxShader, StingrayPBS, Anisotropic, Blinn, Brownian, Bulge, Checker, Cloth, Cloud, Crater, EnvBall, EnvChrome, EnvCube, EnvFog, EnvSky, EnvSphere, File, Fractal, Granite, Grid, HairTubeShader, Lambert, LayeredShader, LayeredTexture, Leather, LightFog, Mandelbrot, Mandelbrot3D, Marble, Mountain, Movie, Noise, Ocean, OceanShader, ParticleCloud, ParticleSamplerInfo, Phong, PhongE, Projection, PsdFileTex, Ramp, RampShader, Rock, ShadingMap, Snow, SolidFractal, StandardSurface, Stencil, Stucco, UseBackground, VolumeFog, VolumeNoise, Water, Wood]
    type_output = Material

    def adapt(self, data: str):
        return Material(data)
