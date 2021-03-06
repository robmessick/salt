# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Erik Johnson (erik@saltstack.com)`
    tests.integration.states.npm
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Import Salt Testing libs
from salttesting import skipIf
from salttesting.helpers import destructiveTest, ensure_in_syspath
ensure_in_syspath('../../')

# Import salt libs
import integration
import salt.utils


@skipIf(salt.utils.which('npm') is None, 'npm not installed')
class NpmStateTest(integration.ModuleCase, integration.SaltReturnAssertsMixIn):

    @destructiveTest
    def test_npm_installed_removed(self):
        '''
        Basic test to determine if NPM module was successfully installed and
        removed.
        '''
        ret = self.run_state('npm.installed', name='pm2')
        self.assertSaltTrueReturn(ret)
        ret = self.run_state('npm.removed', name='pm2')
        self.assertSaltTrueReturn(ret)


if __name__ == '__main__':
    from integration import run_tests
    run_tests(NpmStateTest)
