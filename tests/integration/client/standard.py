# -*- coding: utf-8 -*-

# Import Salt Testing libs
from salttesting.helpers import ensure_in_syspath
ensure_in_syspath('../../')

# Import salt libs
import integration


class StdTest(integration.ModuleCase):
    '''
    Test standard client calls
    '''

    def test_cli(self):
        '''
        Test cli function
        '''
        cmd_iter = self.client.cmd_cli(
                'minion',
                'test.ping',
                )
        for ret in cmd_iter:
            self.assertTrue(ret['minion'])

    def test_iter(self):
        '''
        test cmd_iter
        '''
        cmd_iter = self.client.cmd_iter(
                'minion',
                'test.ping',
                )
        for ret in cmd_iter:
            self.assertTrue(ret['minion'])

    def test_iter_no_block(self):
        '''
        test cmd_iter_no_block
        '''
        cmd_iter = self.client.cmd_iter_no_block(
                'minion',
                'test.ping',
                )
        for ret in cmd_iter:
            if ret is None:
                continue
            self.assertTrue(ret['minion'])

    def test_full_returns(self):
        '''
        test cmd_iter
        '''
        ret = self.client.cmd_full_return(
                'minion',
                'test.ping',
                )
        self.assertIn('minion', ret)
        self.assertEqual({'ret': True, 'success': True}, ret['minion'])

        ret = self.client.cmd_full_return(
                'minion',
                'test.pong',
                )
        self.assertIn('minion', ret)

        if self.master_opts['transport'] == 'zeromq':
            self.assertEqual(
                {
                    'out': 'nested',
                    'ret': '\'test.pong\' is not available.',
                    'success': False
                },
                ret['minion']
            )
        elif self.master_opts['transport'] == 'raet':
            self.assertEqual(
                {'success': False, 'ret': '\'test.pong\' is not available.'},
                ret['minion']
            )

if __name__ == '__main__':
    from integration import run_tests
    run_tests(StdTest)
