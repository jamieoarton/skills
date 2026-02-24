# Edit Key Result

Update a Target.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/key_result/{key_result_id}": {
      "put": {
        "summary": "Edit Key Result",
        "tags": [
          "Goals"
        ],
        "description": "Update a Target.",
        "operationId": "EditKeyResult",
        "parameters": [
          {
            "name": "key_result_id",
            "in": "path",
            "description": "8480-49bc-8c57-e569747efe93 (uuid)",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "947d46ed"
              ]
            }
          }
        ],
        "requestBody": {
          "description": "All properties available in the Create Key Result endpoint may also be used along with the additional properties below.",
          "content": {
            "application/json": {
              "schema": {
                "title": "EditKeyResultrequest",
                "required": [
                  "steps_current",
                  "note"
                ],
                "type": "object",
                "properties": {
                  "steps_current": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  },
                  "note": {
                    "type": "string"
                  }
                },
                "examples": [
                  {
                    "steps_current": 5,
                    "note": "Target achieved"
                  }
                ]
              },
              "example": {
                "steps_current": 5,
                "note": "Target achieved"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "EditKeyResultresponse",
                  "required": [
                    "key_result"
                  ],
                  "type": "object",
                  "properties": {
                    "key_result": {
                      "title": "KeyResult1",
                      "required": [
                        "id",
                        "goal_id",
                        "name",
                        "type",
                        "unit",
                        "creator",
                        "date_created",
                        "goal_pretty_id",
                        "percent_completed",
                        "completed",
                        "task_ids",
                        "subcategory_ids",
                        "owners",
                        "last_action"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "goal_id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        },
                        "unit": {
                          "type": "string"
                        },
                        "creator": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "date_created": {
                          "type": "string"
                        },
                        "goal_pretty_id": {
                          "type": "string"
                        },
                        "percent_completed": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "completed": {
                          "type": "boolean"
                        },
                        "task_ids": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "subcategory_ids": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "owners": {
                          "type": "array",
                          "items": {
                            "$ref": "#/paths/~1v2~1goal~1%7Bgoal_id%7D/get/responses/200/content/application~1json/schema/properties/goal/properties/owners/items"
                          },
                          "description": ""
                        },
                        "last_action": {
                          "title": "LastAction1",
                          "required": [
                            "id",
                            "key_result_id",
                            "userid",
                            "date_modified",
                            "steps_taken",
                            "note",
                            "steps_before",
                            "steps_current",
                            "steps_before_float",
                            "steps_taken_float",
                            "steps_current_float"
                          ],
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "key_result_id": {
                              "type": "string"
                            },
                            "userid": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "date_modified": {
                              "type": "string"
                            },
                            "steps_taken": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "note": {
                              "type": "string"
                            },
                            "steps_before": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "steps_current": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "steps_before_float": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "steps_taken_float": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "steps_current_float": {
                              "type": [
                                "string",
                                "null"
                              ]
                            }
                          },
                          "examples": [
                            {
                              "id": "e889858b-a023-46cc-968a-cac32fd04c1e",
                              "key_result_id": "19c7a55e-537e-4bc9-b741-08df05a5bda8",
                              "userid": 183,
                              "date_modified": "1568122776851",
                              "steps_taken": null,
                              "note": "Target achieved",
                              "steps_before": null,
                              "steps_current": null,
                              "steps_before_float": 0,
                              "steps_taken_float": 5,
                              "steps_current_float": null
                            }
                          ]
                        }
                      },
                      "examples": [
                        {
                          "id": "947d46ed-8480-49bc-8c57-e569747efe93",
                          "goal_id": "e53a033c-900e-462d-a849-4a216b06d930",
                          "name": "New Key Result Name",
                          "type": "number",
                          "unit": "km",
                          "creator": 183,
                          "date_created": "1568062902048",
                          "goal_pretty_id": "6",
                          "percent_completed": null,
                          "completed": false,
                          "task_ids": [],
                          "subcategory_ids": [],
                          "owners": [
                            {
                              "id": 183,
                              "username": "John Doe",
                              "email": "example@email.com",
                              "color": "#827718",
                              "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg",
                              "initials": "JK"
                            }
                          ],
                          "last_action": {
                            "id": "e889858b-a023-46cc-968a-cac32fd04c1e",
                            "key_result_id": "19c7a55e-537e-4bc9-b741-08df05a5bda8",
                            "userid": 183,
                            "date_modified": "1568122776851",
                            "steps_taken": null,
                            "note": "Target achieved",
                            "steps_before": null,
                            "steps_current": null,
                            "steps_before_float": 0,
                            "steps_taken_float": 5,
                            "steps_current_float": null
                          }
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "key_result": {
                        "id": "947d46ed-8480-49bc-8c57-e569747efe93",
                        "goal_id": "e53a033c-900e-462d-a849-4a216b06d930",
                        "name": "New Key Result Name",
                        "type": "number",
                        "unit": "km",
                        "creator": 183,
                        "date_created": "1568062902048",
                        "goal_pretty_id": "6",
                        "percent_completed": null,
                        "completed": false,
                        "task_ids": [],
                        "subcategory_ids": [],
                        "owners": [
                          {
                            "id": 183,
                            "username": "John Doe",
                            "email": "example@email.com",
                            "color": "#827718",
                            "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg",
                            "initials": "JK"
                          }
                        ],
                        "last_action": {
                          "id": "e889858b-a023-46cc-968a-cac32fd04c1e",
                          "key_result_id": "19c7a55e-537e-4bc9-b741-08df05a5bda8",
                          "userid": 183,
                          "date_modified": "1568122776851",
                          "steps_taken": null,
                          "note": "Target achieved",
                          "steps_before": null,
                          "steps_current": null,
                          "steps_before_float": 0,
                          "steps_taken_float": 5,
                          "steps_current_float": null
                        }
                      }
                    }
                  ]
                },
                "example": {
                  "key_result": {
                    "id": "947d46ed-8480-49bc-8c57-e569747efe93",
                    "goal_id": "e53a033c-900e-462d-a849-4a216b06d930",
                    "name": "New Key Result Name",
                    "type": "number",
                    "unit": "km",
                    "creator": 183,
                    "date_created": "1568062902048",
                    "goal_pretty_id": "6",
                    "percent_completed": null,
                    "completed": false,
                    "task_ids": [],
                    "subcategory_ids": [],
                    "owners": [
                      {
                        "id": 183,
                        "username": "John Doe",
                        "email": "example@email.com",
                        "color": "#827718",
                        "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg",
                        "initials": "JK"
                      }
                    ],
                    "last_action": {
                      "id": "e889858b-a023-46cc-968a-cac32fd04c1e",
                      "key_result_id": "19c7a55e-537e-4bc9-b741-08df05a5bda8",
                      "userid": 183,
                      "date_modified": "1568122776851",
                      "steps_taken": null,
                      "note": "Target achieved",
                      "steps_before": null,
                      "steps_current": null,
                      "steps_before_float": 0,
                      "steps_taken_float": 5,
                      "steps_current_float": null
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Goals"
    }
  ]
}
```