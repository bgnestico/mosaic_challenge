
describe('User Login', () => {
  it('should be able to login', () => {

    cy.visit('url to the login page')
    cy.get('#username').type('username')
    cy.get('#password').type('password')
    cy.contains('Login').click()

    cy.url().should('eq', 'url to the home page');
    cy.get('username-element').should('exist');
    expect('user-account-avatar-element').to.be.visible()
  })
})
