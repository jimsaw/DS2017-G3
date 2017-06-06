import menu as me
import CSV
import usuario as us
import platillo as pla

usu = us.Usuario("Kevin", "Bolasdemadera", "Administrador", "None")
pla = pla.Platillo("a","dasdas", "dasdas", "dasdas", "dass", "dasa")
usu.setNombre("Jose")
l = CSV.devolverPlatillos()
for i in l:
    print(i)
dicc = me.busquedaCategoria(l)
me.listarCategoria(dicc)
#me.menuPrincipal(usu)