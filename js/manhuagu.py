__all__ = ['manhuagu']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['pyf', 'LZString'])
@Js
def PyJsHoisted_pyf_(x, this, arguments, var=var):
    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
    var.registers(['x'])
    return var.get('LZString').callprop('decompressFromBase64', var.get('x'))
PyJsHoisted_pyf_.func_name = 'pyf'
var.put('pyf', PyJsHoisted_pyf_)
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['f', 'baseReverseDic', 'getBaseValue', 'LZString', 'keyStrBase64'])
    @Js
    def PyJsHoisted_getBaseValue_(alphabet, character, this, arguments, var=var):
        var = Scope({'alphabet':alphabet, 'character':character, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'character', 'alphabet'])
        if var.get('baseReverseDic').get(var.get('alphabet')).neg():
            var.get('baseReverseDic').put(var.get('alphabet'), Js({}))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('alphabet').get('length')):
                var.get('baseReverseDic').get(var.get('alphabet')).put(var.get('alphabet').callprop('charAt', var.get('i')), var.get('i'))
                # update
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return var.get('baseReverseDic').get(var.get('alphabet')).get(var.get('character'))
    PyJsHoisted_getBaseValue_.func_name = 'getBaseValue'
    var.put('getBaseValue', PyJsHoisted_getBaseValue_)
    var.put('f', var.get('String').get('fromCharCode'))
    var.put('keyStrBase64', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='))
    var.put('baseReverseDic', Js({}))
    pass
    @Js
    def PyJs_anonymous_1_(input, this, arguments, var=var):
        var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
        var.registers(['input'])
        if (var.get('input')==var.get(u"null")):
            return Js('')
        if (var.get('input')==Js('')):
            return var.get(u"null")
        @Js
        def PyJs_anonymous_2_(index, this, arguments, var=var):
            var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
            var.registers(['index'])
            return var.get('getBaseValue')(var.get('keyStrBase64'), var.get('input').callprop('charAt', var.get('index')))
        PyJs_anonymous_2_._set_name('anonymous')
        return var.get('LZString').callprop('_0', var.get('input').get('length'), Js(32.0), PyJs_anonymous_2_)
    PyJs_anonymous_1_._set_name('anonymous')
    @Js
    def PyJs_anonymous_3_(length, resetValue, getNextValue, this, arguments, var=var):
        var = Scope({'length':length, 'resetValue':resetValue, 'getNextValue':getNextValue, 'this':this, 'arguments':arguments}, var)
        var.registers(['resetValue', 'numBits', 'enlargeIn', 'dictSize', 'w', 'maxpower', 'dictionary', 'bits', 'data', 'resb', 'getNextValue', 'length', 'entry', 'next', 'result', 'i', 'power', 'c'])
        var.put('dictionary', Js([]))
        var.put('enlargeIn', Js(4.0))
        var.put('dictSize', Js(4.0))
        var.put('numBits', Js(3.0))
        var.put('entry', Js(''))
        var.put('result', Js([]))
        var.put('data', Js({'val':var.get('getNextValue')(Js(0.0)),'position':var.get('resetValue'),'index':Js(1.0)}))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<Js(3.0)):
            var.get('dictionary').put(var.get('i'), var.get('i'))
            # update
            var.put('i', Js(1.0), '+')
        var.put('bits', Js(0.0))
        var.put('maxpower', var.get('Math').callprop('pow', Js(2.0), Js(2.0)))
        var.put('power', Js(1.0))
        while (var.get('power')!=var.get('maxpower')):
            var.put('resb', (var.get('data').get('val')&var.get('data').get('position')))
            var.get('data').put('position', Js(1.0), '>>')
            if (var.get('data').get('position')==Js(0.0)):
                var.get('data').put('position', var.get('resetValue'))
                var.get('data').put('val', var.get('getNextValue')((var.get('data').put('index',Js(var.get('data').get('index').to_number())+Js(1))-Js(1))))
            var.put('bits', ((Js(1.0) if (var.get('resb')>Js(0.0)) else Js(0.0))*var.get('power')), '|')
            var.put('power', Js(1.0), '<<')
        while 1:
            SWITCHED = False
            CONDITION = (var.put('next', var.get('bits')))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                SWITCHED = True
                var.put('bits', Js(0.0))
                var.put('maxpower', var.get('Math').callprop('pow', Js(2.0), Js(8.0)))
                var.put('power', Js(1.0))
                while (var.get('power')!=var.get('maxpower')):
                    var.put('resb', (var.get('data').get('val')&var.get('data').get('position')))
                    var.get('data').put('position', Js(1.0), '>>')
                    if (var.get('data').get('position')==Js(0.0)):
                        var.get('data').put('position', var.get('resetValue'))
                        var.get('data').put('val', var.get('getNextValue')((var.get('data').put('index',Js(var.get('data').get('index').to_number())+Js(1))-Js(1))))
                    var.put('bits', ((Js(1.0) if (var.get('resb')>Js(0.0)) else Js(0.0))*var.get('power')), '|')
                    var.put('power', Js(1.0), '<<')
                var.put('c', var.get('f')(var.get('bits')))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                SWITCHED = True
                var.put('bits', Js(0.0))
                var.put('maxpower', var.get('Math').callprop('pow', Js(2.0), Js(16.0)))
                var.put('power', Js(1.0))
                while (var.get('power')!=var.get('maxpower')):
                    var.put('resb', (var.get('data').get('val')&var.get('data').get('position')))
                    var.get('data').put('position', Js(1.0), '>>')
                    if (var.get('data').get('position')==Js(0.0)):
                        var.get('data').put('position', var.get('resetValue'))
                        var.get('data').put('val', var.get('getNextValue')((var.get('data').put('index',Js(var.get('data').get('index').to_number())+Js(1))-Js(1))))
                    var.put('bits', ((Js(1.0) if (var.get('resb')>Js(0.0)) else Js(0.0))*var.get('power')), '|')
                    var.put('power', Js(1.0), '<<')
                var.put('c', var.get('f')(var.get('bits')))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                SWITCHED = True
                return Js('')
            SWITCHED = True
            break
        var.get('dictionary').put('3', var.get('c'))
        var.put('w', var.get('c'))
        var.get('result').callprop('push', var.get('c'))
        while Js(True):
            if (var.get('data').get('index')>var.get('length')):
                return Js('')
            var.put('bits', Js(0.0))
            var.put('maxpower', var.get('Math').callprop('pow', Js(2.0), var.get('numBits')))
            var.put('power', Js(1.0))
            while (var.get('power')!=var.get('maxpower')):
                var.put('resb', (var.get('data').get('val')&var.get('data').get('position')))
                var.get('data').put('position', Js(1.0), '>>')
                if (var.get('data').get('position')==Js(0.0)):
                    var.get('data').put('position', var.get('resetValue'))
                    var.get('data').put('val', var.get('getNextValue')((var.get('data').put('index',Js(var.get('data').get('index').to_number())+Js(1))-Js(1))))
                var.put('bits', ((Js(1.0) if (var.get('resb')>Js(0.0)) else Js(0.0))*var.get('power')), '|')
                var.put('power', Js(1.0), '<<')
            while 1:
                SWITCHED = False
                CONDITION = (var.put('c', var.get('bits')))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    var.put('bits', Js(0.0))
                    var.put('maxpower', var.get('Math').callprop('pow', Js(2.0), Js(8.0)))
                    var.put('power', Js(1.0))
                    while (var.get('power')!=var.get('maxpower')):
                        var.put('resb', (var.get('data').get('val')&var.get('data').get('position')))
                        var.get('data').put('position', Js(1.0), '>>')
                        if (var.get('data').get('position')==Js(0.0)):
                            var.get('data').put('position', var.get('resetValue'))
                            var.get('data').put('val', var.get('getNextValue')((var.get('data').put('index',Js(var.get('data').get('index').to_number())+Js(1))-Js(1))))
                        var.put('bits', ((Js(1.0) if (var.get('resb')>Js(0.0)) else Js(0.0))*var.get('power')), '|')
                        var.put('power', Js(1.0), '<<')
                    var.get('dictionary').put((var.put('dictSize',Js(var.get('dictSize').to_number())+Js(1))-Js(1)), var.get('f')(var.get('bits')))
                    var.put('c', (var.get('dictSize')-Js(1.0)))
                    (var.put('enlargeIn',Js(var.get('enlargeIn').to_number())-Js(1))+Js(1))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('bits', Js(0.0))
                    var.put('maxpower', var.get('Math').callprop('pow', Js(2.0), Js(16.0)))
                    var.put('power', Js(1.0))
                    while (var.get('power')!=var.get('maxpower')):
                        var.put('resb', (var.get('data').get('val')&var.get('data').get('position')))
                        var.get('data').put('position', Js(1.0), '>>')
                        if (var.get('data').get('position')==Js(0.0)):
                            var.get('data').put('position', var.get('resetValue'))
                            var.get('data').put('val', var.get('getNextValue')((var.get('data').put('index',Js(var.get('data').get('index').to_number())+Js(1))-Js(1))))
                        var.put('bits', ((Js(1.0) if (var.get('resb')>Js(0.0)) else Js(0.0))*var.get('power')), '|')
                        var.put('power', Js(1.0), '<<')
                    var.get('dictionary').put((var.put('dictSize',Js(var.get('dictSize').to_number())+Js(1))-Js(1)), var.get('f')(var.get('bits')))
                    var.put('c', (var.get('dictSize')-Js(1.0)))
                    (var.put('enlargeIn',Js(var.get('enlargeIn').to_number())-Js(1))+Js(1))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    return var.get('result').callprop('join', Js(''))
                SWITCHED = True
                break
            if (var.get('enlargeIn')==Js(0.0)):
                var.put('enlargeIn', var.get('Math').callprop('pow', Js(2.0), var.get('numBits')))
                (var.put('numBits',Js(var.get('numBits').to_number())+Js(1))-Js(1))
            if var.get('dictionary').get(var.get('c')):
                var.put('entry', var.get('dictionary').get(var.get('c')))
            else:
                if PyJsStrictEq(var.get('c'),var.get('dictSize')):
                    var.put('entry', (var.get('w')+var.get('w').callprop('charAt', Js(0.0))))
                else:
                    return var.get(u"null")
            var.get('result').callprop('push', var.get('entry'))
            var.get('dictionary').put((var.put('dictSize',Js(var.get('dictSize').to_number())+Js(1))-Js(1)), (var.get('w')+var.get('entry').callprop('charAt', Js(0.0))))
            (var.put('enlargeIn',Js(var.get('enlargeIn').to_number())-Js(1))+Js(1))
            var.put('w', var.get('entry'))
            if (var.get('enlargeIn')==Js(0.0)):
                var.put('enlargeIn', var.get('Math').callprop('pow', Js(2.0), var.get('numBits')))
                (var.put('numBits',Js(var.get('numBits').to_number())+Js(1))-Js(1))
    PyJs_anonymous_3_._set_name('anonymous')
    var.put('LZString', Js({'decompressFromBase64':PyJs_anonymous_1_,'_0':PyJs_anonymous_3_}))
    return var.get('LZString')
PyJs_anonymous_0_._set_name('anonymous')
var.put('LZString', PyJs_anonymous_0_())
pass
pass


# Add lib to the module scope
manhuagu = var.to_python()