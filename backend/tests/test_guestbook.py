from ferrisnose import EndpointsTest
from app.guestbook import guestbook_service


class TestGuestbook(EndpointsTest):

    def test_api(self):
        self.add_service(guestbook_service.GuestbookService)

        resp = self.invoke('GuestbookService.insert', {
            "content": "hello!"
        })

        assert resp['content'] == 'hello!'

        resp = self.invoke('GuestbookService.list')

        assert len(resp['items']) == 1
        assert resp['items'][0]['content'] == 'hello!'
